import { TestBed, inject } from '@angular/core/testing';

import { BloggerService } from './blogger.service';

describe('BloggerService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [BloggerService]
    });
  });

  it('should be created', inject([BloggerService], (service: BloggerService) => {
    expect(service).toBeTruthy();
  }));
});
