import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { TaskService } from 'src/app/services/task.service';

@Component({
  selector: 'app-add-new-list-form',
  templateUrl: './add-new-list-form.component.html',
  styleUrls: ['./add-new-list-form.component.css']
})
export class AddNewListFormComponent {
  listForm!: FormGroup;

  constructor(private formBuilder: FormBuilder,
              private taskService: TaskService,
              private router: Router) { }

  ngOnInit(): void {
    this.listForm = this.formBuilder.group({
      title: ['', Validators.required],
    });
  }

  get f() { return this.listForm.controls; }

  onSubmit() {
    if (this.listForm.invalid) {
      return;
    }

    this.taskService.createNewList(this.f["title"].value)
                    .subscribe(response => {
                      let new_list = response['list'];
                      this.router.navigateByUrl('/list/'+new_list['listId']);
                    })
  }

}
