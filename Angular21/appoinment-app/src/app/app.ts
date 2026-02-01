import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { AppoinmentList } from "./appoinment-list/appoinment-list";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, AppoinmentList],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('appoinment-app');
}
