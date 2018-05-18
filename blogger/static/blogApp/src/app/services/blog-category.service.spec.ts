import { TestBed, inject } from '@angular/core/testing';

import { BlogCategoryService } from './blog-category.service';

describe('BlogCategoryService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [BlogCategoryService]
    });
  });

  it('should be created', inject([BlogCategoryService], (service: BlogCategoryService) => {
    expect(service).toBeTruthy();
  }));
});
