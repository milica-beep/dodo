import { Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  opened: boolean = false;
  currentDate: Date = new Date();

  constructor(private authService: AuthService) {}

  ngOnInit() {
  }
}
