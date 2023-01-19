import { Component } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { TaskService } from 'src/app/services/task.service';

@Component({
  selector: 'app-sidebar-content',
  templateUrl: './sidebar-content.component.html',
  styleUrls: ['./sidebar-content.component.css']
})
export class SidebarContentComponent {
  lists = [];
  showAddNewListForm: boolean = false;

  constructor(private taskService: TaskService,
              private authService: AuthService,
              private router: Router) { }

  ngOnInit(): void {
    this.taskService.getLists().subscribe((response) => {
      this.lists = response['lists'];
    })

    this.router.events.subscribe(val => {
      if(val instanceof NavigationEnd) {

          this.taskService.getLists().subscribe((response) => {
            this.lists = response['lists'];
          })
        
      }
    })
  }

  openAddNewListForm() {
    this.showAddNewListForm = !this.showAddNewListForm;
  }

  removeList(list: any) {
    this.taskService.deleteList(list['listId']).subscribe(response => {
      this.lists = response['lists'];
    })
  }

  onNewListCreated(event: any) {
    this.taskService.getLists().subscribe((response) => {
      this.lists = response['lists'];
    })
  }

  logout() {
    this.authService.logout();
    this.router.navigateByUrl('');
  }

}
