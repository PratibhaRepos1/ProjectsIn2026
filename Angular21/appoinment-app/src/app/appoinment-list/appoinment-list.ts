import { Component } from '@angular/core';
import { Appointment } from '../models/appointment';

@Component({
  selector: 'app-appoinment-list',
  imports: [],
  templateUrl: './appoinment-list.html',
  styleUrl: './appoinment-list.css',
})
export class AppoinmentList {
appoinment: Appointment = {
  id:1,
  title: "Take dog for a walk",
  date: new Date("2026-02-01")
}

}
