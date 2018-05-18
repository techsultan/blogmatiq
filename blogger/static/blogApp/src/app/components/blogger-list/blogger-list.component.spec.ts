import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BloggerListComponent } from './blogger-list.component';

describe('BloggerListComponent', () => {
  let component: BloggerListComponent;
  let fixture: ComponentFixture<BloggerListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BloggerListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BloggerListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
