import { Component, ViewChild } from '@angular/core';
import { MatCalendar } from '@angular/material/datepicker';


@Component({
  selector: 'app-calendar-component',
  templateUrl: './calendar-component.component.html',
  styleUrls: ['./calendar-component.component.css']
})
export class CalendarComponentComponent {
  selected!: Date | null;
}
