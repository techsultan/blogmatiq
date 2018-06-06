import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
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
import { BlogDetailComponent } from './components/blog-detail/blog-detail.component';
import { BloggerDetailComponent } from './components/blogger-detail/blogger-detail.component';
import { RecentPostsComponent } from './components/recent-posts/recent-posts.component';

//Import all custom modules
import { BlogRoutingModule } from './modules/blog-routing/blog-routing.module';
import { MaterialModule } from './modules/material/material.module';

/* Import the API Services used by blogApp*/
import {  }
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
    BloggerDetailComponent,
    RecentPostsComponent
  ],
  imports: [
    BrowserModule, BlogRoutingModule, MaterialModule, BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
