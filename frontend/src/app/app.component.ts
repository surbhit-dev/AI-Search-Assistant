import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SearchBoxComponent } from './components/search-box/search-box.component';
import { AnswerBoxComponent } from './components/answer-box/answer-box.component';
import { SourceListComponent } from './components/source-list/source-list.component';
import { SearchService } from './services/search.service';
import { FlameComponent } from './components/flame/flame.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    SearchBoxComponent,
    AnswerBoxComponent,
    SourceListComponent,
    FlameComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {

  answer = '';
  sources: string[] = [];
  loading = false;

  constructor(
    private searchService: SearchService
  ) {}

  onSearch(query: string) {

    this.loading = true;

    this.searchService.search(query)
      .subscribe((response: any) => {

        this.answer = response.answer;

        this.sources = response.sources.map(
          (item: any) => item.title
        );

        this.loading = false;

      });

  }

}