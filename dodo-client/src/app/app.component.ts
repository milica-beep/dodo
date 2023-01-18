import { Component } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';
import { AuthService } from './services/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'dodo-client';
  opened: boolean | undefined;

  constructor(private authService: AuthService,
              private router: Router) {}

  ngOnInit() {
    this.router.events.subscribe(val => {
      if(val instanceof NavigationEnd) {
        if(val['url'] == '/home' || val['url'] == '/') {
          this.authService.getCurrentUser().subscribe({
            error: (e) => this.opened = false,
            complete: () => this.opened = true 
          });
        }

      }
    })

    // this.authService.getCurrentUser().subscribe({
    //   error: (e) => this.opened = false,
    //   complete: () => this.opened = true 
    // });
  }
}
