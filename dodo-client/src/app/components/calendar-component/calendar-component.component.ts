import { Component, Input, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatCalendar } from '@angular/material/datepicker';
import { ActivatedRoute, NavigationEnd, Router } from '@angular/router';
import { TaskByDate } from 'src/app/models/taskByDate';
import { TaskService } from 'src/app/services/task.service';
import { DatePipe } from '@angular/common';


@Component({
  selector: 'app-calendar-component',
  templateUrl: './calendar-component.component.html',
  styleUrls: ['./calendar-component.component.css']
})
export class CalendarComponentComponent {
  selectedDate: Date = new Date();
  tasks: TaskByDate[] = [];
  taskForm!: FormGroup;

  constructor(private taskService: TaskService,
    private route: ActivatedRoute,
    private formBuilder: FormBuilder,
    private datepipe: DatePipe) { }

    ngOnInit(): void {
      this.taskForm = this.formBuilder.group({
        task: ['', Validators.required],
      });

      if(this.selectedDate) {
        this.taskService.getTasks(this.datepipe.transform(this.selectedDate, 'yyyy-MM-dd')).subscribe((response) => {
          this.tasks = response['tasks'];
        })
      }
        
    }
  
    get f() { return this.taskForm.controls; }

  dateChanged(event: any) {
    this.taskService.getTasks(this.datepipe.transform(this.selectedDate, 'yyyy-MM-dd')).subscribe((response) => {
      this.tasks = response['tasks'];
    })
  }

  removeTask(task: TaskByDate) {
    this.taskService.deleteTask(task.taskId, this.datepipe.transform(this.selectedDate, 'yyyy-MM-dd')).subscribe(response => {
      this.tasks = response['tasks'];
    })
  }

  onChange(taskId:string) {
    this.taskService.completeTask(taskId, this.datepipe.transform(this.selectedDate, 'yyyy-MM-dd')).subscribe((response) => {
      let updatedTask = response['task'];
      console.log(this.tasks)
      this.tasks.forEach((element, index) => {
        if(element['taskId'] == taskId) {
          this.tasks[index] = updatedTask;
        }
      });
      console.log("after change",this.tasks)
    });
  }

  onSubmit() {
    if (this.taskForm.invalid) {
      return;
    }

    this.taskService.createNewDateTask(this.datepipe.transform(this.selectedDate, 'yyyy-MM-dd'), this.f["task"].value)
                    .subscribe(response => {
                      this.tasks = response['tasks'];
    })
  }
}
