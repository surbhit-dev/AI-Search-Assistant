import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FormsModule,}  from '@angular/forms';

@Component({
  selector: 'app-search-box',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './search-box.component.html',
  styleUrl: './search-box.component.css'
})
export class SearchBoxComponent {

  @Input()
  title = "";

  query = "";

  @Output()
  searchClicked = new EventEmitter<string>();

  search() {

    this.searchClicked.emit(this.query);

}
}
