import { Component } from '@angular/core';
import { AnimationOptions } from 'ngx-lottie';
import { LottieComponent } from 'ngx-lottie';

@Component({
  selector: 'app-flame',
  standalone: true,
  imports: [LottieComponent],
  templateUrl: './flame.component.html',
  styleUrl: './flame.component.css'
})
export class FlameComponent {

  options: AnimationOptions = {
    path: 'flames.json'
  };

}