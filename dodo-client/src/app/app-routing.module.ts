import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CalendarComponentComponent } from './components/calendar-component/calendar-component.component';
import { CalendarComponent } from './layouts/calendar/calendar.component';
import { HomeComponent } from './layouts/home/home.component';
import { LandingPageComponent } from './layouts/landing-page/landing-page.component';
import { TodoListComponent } from './layouts/todo-list/todo-list.component';

const routes: Routes = [
  { path: '', component: LandingPageComponent},
  { path: 'home', component: HomeComponent },
  { path: 'list/:id/:name', component: TodoListComponent },
  { path: 'calendar', component: CalendarComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
