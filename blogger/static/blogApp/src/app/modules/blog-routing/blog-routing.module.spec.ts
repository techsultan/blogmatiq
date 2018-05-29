import { BlogRoutingModule } from './blog-routing.module';

describe('BlogRoutingModule', () => {
  let blogRoutingModule: BlogRoutingModule;

  beforeEach(() => {
    blogRoutingModule = new BlogRoutingModule();
  });

  it('should create an instance', () => {
    expect(blogRoutingModule).toBeTruthy();
  });
});
