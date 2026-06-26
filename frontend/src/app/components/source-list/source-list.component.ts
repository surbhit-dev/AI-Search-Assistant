import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-source-list',
  standalone: true,
  imports: [],
  templateUrl: './source-list.component.html',
  styleUrl: './source-list.component.css'
})
export class SourceListComponent {

  @Input()
  sources: string[] = [];

}
