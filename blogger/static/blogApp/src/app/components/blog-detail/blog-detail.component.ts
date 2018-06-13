import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import { Router } from '@angular/router';
import { Location } from '@angular/common';
import { BlogService } from '../../services/blog.service';
import { BlogPostService } from '../../services/blog-post.service';
import { BlogCategoryService } from '../../services/blog-category.service';
import { Blog } from '../../classes/blog';

//Import the mock data to use during dev
import { BLOG_DETAILS } from '../../mock-data/blog';
import { CATEGORY_LIST } from '../../mock-data/blog_categories';
import { BLOG_POSTS, BLOG_POST } from '../../mock-data/blog_post'; 


@Component({
  selector: 'app-blog-detail',
  templateUrl: './blog-detail.component.html',
  styleUrls: ['./blog-detail.component.css']
})
export class BlogDetailComponent implements OnInit {
  blogUrl:string;
  blog:any;
  blog_error_message:string;
  category_list_error_message:string;
  blog_posts_error_message:string;
  delete_category_error_message:string;
  blog_posts;
  category_list;
  mock_category_list:string[] = ['Tech Kalam', 'Tastes of the East', 'Rhythms of Africa'];

  constructor(private blogService: BlogService, private blogPostService: BlogPostService, 
    private route: ActivatedRoute, private location: Location, private router:Router, private categoryService: BlogCategoryService) { 
    this.route.params.subscribe(
      params => {
        this.blogUrl = params.blogUrl;
      },
      err => {},
      () => {
        console.log("Done trying to retrieve :blogUrl from ActivateeRoute.params.")
      }
    )
  }

  ngOnInit() {
    this.getBlogDetails();
    this.getCategories();
    //this.getPostsinBlog();
  }

  getBlogDetails(){
    this.blogService.getBlogByUrl(this.blogUrl).subscribe(
      res => {
        this.blog = res;
        console.log("BlogDetailComponent.getBlogDetails() =" + this.blog.page);
      },
      err => {
        this.blog_error_message = err.message;
        this.blog = BLOG_DETAILS;
      },
      () => {
        console.log("BlogService.getBlogByUrl() finished running.");
      }
    )
  }

  goBack():void {
    this.location.back();
  }

  gotoBlogsHome():void{
    this.router.navigate(['blogs']);
  }

  getCategories(){
    this.categoryService.getCategoriesByBlog(this.blogUrl).subscribe(
      res => {
        this.category_list = res;
        console.log(this.category_list);
      },
      err => {
        this.category_list_error_message = err.message;
        //this.category_list = CATEGORY_LIST;
      },
      () => {
        console.log("BlogDetailComponent.getCategories() done running.");
      }
    )
  }

  getPostsinBlog(){
    this.blogPostService.getPostsinBlog(this.blogUrl).subscribe(
      res => {
        this.blog_posts = res;
      },
      err => {
        this.blog_posts_error_message = err.message;
        this.blog_posts = BLOG_POSTS;
      },
      () => {
        console.log("BlogDetailComponent.getPostsinBlog() done running.")
      }
    )
  }

  deleteCategory(categoryUrl){
    this.categoryService.deleteCategory(categoryUrl).subscribe(
      res => {},
      err => {
        this.delete_category_error_message = err.message;
      },
      () => {
        //Removable before deployment.
        console.log("BlogDetailComponent.deleteCategory() run...");
      }
    )
  }

}
