import { Component } from "@angular/core";

@Component({
    selector: 'app-counter',
    standalone: true,
    templateUrl: './counter.component.html'
})
export class CounterComponent {
    count = 0;

    increment(){
        this.count++;
    }

    decrement() {
        if(this.count > 0) {
             this.count--;
        }
       
    }
}

