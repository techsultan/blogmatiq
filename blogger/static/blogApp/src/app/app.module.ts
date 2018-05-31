import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { BloggerComponent } from './components/blogger/blogger.component';
import { BlogCategoryComponent } from './components/blog-category/blog-category.component';
import { BlogPostComponent } from './components/blog-post/blog-post.component';
import { CommentComponent } from './components/comment/comment.component';
import { BlogListComponent } from './components/blog-list/blog-list.component';
import { BloggerListComponent } from './components/blogger-list/blogger-list.component';
import { CommentListComponent } from './components/comment-list/comment-list.component';
import { HomeComponent } from './components/home/home.component';

//Import all custom modules
import { BlogRoutingModule } from './modules/blog-routing/blog-routing.module';
import { BlogDetailComponent } from './components/blog-detail/blog-detail.component';
import { BloggerDetailComponent } from './components/blogger-detail/blogger-detail.component';

//Import thirdparty modules 

@NgModule({
  declarations: [
    AppComponent,
    BloggerComponent,
    BlogCategoryComponent,
    BlogPostComponent,
    CommentComponent,
    BlogListComponent,
    BloggerListComponent,
    CommentListComponent,
    HomeComponent,
    BlogDetailComponent,
    BloggerDetailComponent
  ],
  imports: [
    BrowserModule, BlogRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
