import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {FormsModule } from '@angular/forms';
import { Counter } from './components/counter/counter';


@Component({
  selector: 'app-root',
  imports: [RouterOutlet, FormsModule, Counter],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  protected readonly title = signal('profile-card');
  name: string = 'John Doe';
  age: number = 30;
  description: string = 'A passionate developer learning Angular';
   

}
