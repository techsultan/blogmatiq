import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import { Router } from '@angular/router';
import { Location } from '@angular/common';


import { BlogCategory } from '../../classes/blog-category';
import { BlogCategoryService } from '../../services/blog-category.service';
import { BlogPostService } from '../../services/blog-post.service';
//Mock data to use during dev and testing
import {CATEGORY_LIST} from '../../mock-data/blog_categories';
import {CATEGORY_ITEM} from '../../mock-data/blog_categories';

@Component({
  selector: 'app-blog-category',
  templateUrl: './blog-category.component.html',
  styleUrls: ['./blog-category.component.css']
})
export class BlogCategoryComponent implements OnInit {

  category:any;
  category_posts;
  category_error_message: string;
  posts_error_message:string;
  delete_post_error_message:string;
  delete_post_success_message:string;
  categoryUrl:string;
  parentBlogUrl:string;

  constructor(private categoryService: BlogCategoryService, private postService: BlogPostService,
  private router: Router, private route: ActivatedRoute, private location: Location) {
    this.route.params.subscribe(
      params => {
        this.categoryUrl = params.categoryUrl;
        this.parentBlogUrl = params.blogUrl;
      }
    )
   }

  ngOnInit() {
    this.getCategoryDetails();
    this.getBlogPostsinCategory();
  }

  getCategoryDetails(){
    this.categoryService.getCategoryByUrl(this.categoryUrl).subscribe(
      res => {
        this.category = res;
      },
      err => {
        this.category_error_message = err.message;
      },
      () => {
        //REMOVE before deployment
        console.log("BlogCategoryDetailComponent.getCategoryDetails() called.");
      }
    )
  }

  getBlogPostsinCategory(){
    this.postService.getPostsInCategory(this.categoryUrl).subscribe(
      posts => {
        this.category_posts = posts;
        console.log(this.category_posts);
      },
      err => {
        this.posts_error_message = err.message;
      },
      () => {
        //REMOVE before deployment
        console.log("BlogCatgoryDetailComponent.getPostsinCategory() called.");
      }
    )
  }

  deletePost(postUrl){
    this.postService.deletePost(postUrl).subscribe(
      res => {
        this.delete_post_success_message = "Blog Post with URL: " + postUrl + 'deleted';
      },
      err => {
        this.delete_post_error_message = err.message;
      },
      () => {
        //REMOVE before deployment
        console.log("BlogCategoryDetailComponent.deletePost() run...");
      }
    )
  }

  updateCategory(){

  }

  goBack(){
    this.location.back();
  }

  gotoParentBlog(){
    this.router.navigate(['blogs', this.parentBlogUrl]);
  }
}
