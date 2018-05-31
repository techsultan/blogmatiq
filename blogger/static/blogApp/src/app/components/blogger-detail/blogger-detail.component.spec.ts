import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BloggerDetailComponent } from './blogger-detail.component';

describe('BloggerDetailComponent', () => {
  let component: BloggerDetailComponent;
  let fixture: ComponentFixture<BloggerDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BloggerDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BloggerDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
