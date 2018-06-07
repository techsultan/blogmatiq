import { Component, OnInit } from '@angular/core';
//Import the API services needed for this component to request and send data over HTTP.
import { BlogService } from '../../services/blog.service';
import { BlogPostService } from '../../services/blog-post.service';
import { Blog } from '../../classes/blog';
import { Location } from '@angular/common';
import { Router } from '@angular/router';
import { BLOG_LIST } from '../../mock-data/blog_list';

@Component({
  selector: 'app-blog',
  templateUrl: './blog.component.html',
  styleUrls: ['./blog.component.css']
})
export class BlogListComponent implements OnInit {

  constructor(private blogService: BlogService, private blogPostService: BlogPostService,
  private location: Location, private router:Router) { 

  }
  //api_host = this.apiHost.getApiHost();

  title: string = "Blogmatiq";
  blog_list:any;
  blog_error_message:string;
  blog_posts;
  posts_error_message:string;
  

  ngOnInit() {
    this.getBlogList();
    console.log(this.blog_list);
    this.getBlogPosts();
  }

  getBlogList(){
    this.blogService.getAllBlogs().subscribe(
      data => {
        this.blog_list = data;
        console.log("blog_list: " + this.blog_list);
      },
      err => {
        this.blog_list = BLOG_LIST;
        this.blog_error_message = err.message;

      },
      () => {
        //FOR DEBUGGING ONLY: DELETE before deployment.
        console.log("BlogService.getAllBlogs() done running...");
      }
    )
  }

  getBlogPosts(){
    this.blogPostService.getAllPosts().subscribe(
      res => {
        this.blog_posts = res;
      },
      err => {
        this.posts_error_message = err.message;
      },
      () => {
        console.log("BlogComponent.getBlogPosts() done running..");
      }
    )
  }

  gotoHomePage():void {
    this.router.navigate([''])
  }

  createNewBlog(new_blog_data){
    this.blogService.createBlog(new_blog_data).subscribe(
      res => {},
      err => {},
      () => {
        //REMOVE before deployment
        console.log("BlogService.createBlog() called...");
      }
    )
  }

}