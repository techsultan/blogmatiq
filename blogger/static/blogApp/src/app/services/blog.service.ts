import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ApiRootService } from './api-root.service';

@Injectable({
  providedIn: 'root'
})
export class BlogService {
  blogApiUrl:string;
  blog_api_endpoint:string = "/api/blogger/blogs/";

  constructor(private Http: HttpClient, private ApiRoot: ApiRootService) { 
    this.blogApiUrl = this.ApiRoot.getRoot() + this.blog_api_endpoint;
  }

  getAllBlogs(){
   return this.Http.get(this.blogApiUrl);
  }

  getBlogByUrl(blog_url){
    return this.Http.get(this.blogApiUrl + blog_url);
  }

  createBlog(new_blog_data){
    return this.Http.post(this.blogApiUrl, new_blog_data);
  }

  updateBlog(blog_url, updated_blog_data){
    return this.Http.put(this.blogApiUrl, blog_url, updated_blog_data);
  }

  deleteBlog(blog_url){
    return this.Http.delete(this.blogApiUrl + blog_url);
  }

  getBlogsByBlogger(bloggerUrl){
    return this.Http.get(this.blogApiUrl + '?blogger__link=' + bloggerUrl);
  }
  

}
