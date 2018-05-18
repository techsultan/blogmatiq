import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { BloggerComponent } from './components/blogger/blogger.component';
import { BlogComponent } from './components/blog/blog.component';
import { BlogCategoryComponent } from './components/blog-category/blog-category.component';
import { BlogPostComponent } from './components/blog-post/blog-post.component';
import { CommentComponent } from './components/comment/comment.component';
import { BlogListComponent } from './components/blog-list/blog-list.component';
import { BloggerListComponent } from './components/blogger-list/blogger-list.component';
import { CommentListComponent } from './components/comment-list/comment-list.component';

@NgModule({
  declarations: [
    AppComponent,
    BloggerComponent,
    BlogComponent,
    BlogCategoryComponent,
    BlogPostComponent,
    CommentComponent,
    BlogListComponent,
    BloggerListComponent,
    CommentListComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
