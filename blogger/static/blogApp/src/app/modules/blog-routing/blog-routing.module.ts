
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';

//Import all components of blogApp 
import { HomeComponent } from '../../components/home/home.component';
import { BlogListComponent }  from '../../components/blog-list/blog-list.component';
import { BlogDetailComponent } from '../../components/blog-detail/blog-detail.component';
import { BlogCategoryComponent } from '../../components/blog-category/blog-category.component';
import { BlogPostComponent } from '../../components/blog-post/blog-post.component';
import { BloggerListComponent }  from '../../components/blogger-list/blogger-list.component';
import { BloggerDetailComponent } from '../../components/blogger-detail/blogger-detail.component';
import { RecentPostsComponent } from '../../components/recent-posts/recent-posts.component';
//import { CommentListComponent } from '../../components/comment-list/comment-list.component';
//import { CommentComponent } from '../../components/comment/comment.component';



const routes: Routes = [
 {
  path: '',
  component: HomeComponent
 },
 {
   path: 'bloggers',
   component: BloggerListComponent
 },
 {
   path: 'bloggers/:bloggerUrl',
   component: BloggerDetailComponent
 },
 {
   path: 'blogs',
   component: BlogListComponent
 },
 {
   path: 'recent-posts',
   component: RecentPostsComponent
 },
 {
   path: 'blogs/:blogUrl',
   component: BlogDetailComponent
 },
 {
   path: 'blogs/:blogUrl/:categoryUrl',
   component: BlogCategoryComponent
 },
 {
   path: 'blogs/:blogUrl/:categoryUrl/:postUrl',
   component: BlogPostComponent
 }
]

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule],
  declarations: []
})
export class BlogRoutingModule { }
