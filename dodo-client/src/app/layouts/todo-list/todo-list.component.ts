import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { TaskByListId } from 'src/app/models/taskByListId';
import { TaskService } from 'src/app/services/task.service';

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css']
})
export class TodoListComponent {
  tasks: TaskByListId[] = [];
  listId: any = '';
  listName: any = '';
  taskForm!: FormGroup;
  constructor(private taskService: TaskService,
              private route: ActivatedRoute,
              private formBuilder: FormBuilder) { }

  ngOnInit(): void {
    this.taskForm = this.formBuilder.group({
      task: ['', Validators.required],
    });

    this.route.paramMap.subscribe(params => {
      this.listId = params.get('id');
      this.listName = params.get('name');
      this.taskService.getTasksByListId(this.listId).subscribe((response) => {
        this.tasks = response['tasks'];
      })
    });
  }

  get f() { return this.taskForm.controls; }

  onChange(taskId:string) {
    this.taskService.completeTask(taskId, this.listId).subscribe((response) => {
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

    this.taskService.createNewListTask(this.listId, this.f["task"].value)
                    .subscribe(response => {
                      this.tasks = response['tasks'];
                    })
  }
}

