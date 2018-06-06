import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class BlogService {
  bloApiUrl:string = "/api/blogs/";

  constructor(private Http: HttpClient) { }

  getAllBlogs(){
   return this.http.get(this.blogApiUrl);
  }

  getBlogByUrl(blog_url){
    return this.http.get(this.blogApiUrl + blog_url);
  }

  createBlog(new_blog_data){
    return this.http.post(this.blogApiUrl, new_blog_data);
  }

  updateBlog(blog_url, updated_blog_data){
    return this.http.put(this.blogApiUrl, blog_url, updated_blog_data);
  }

  deleteBlog(blog_url){
    return this.http.delete(this.blogApiUrl + blog_url);
  }

  getBlogsByBlogger(bloggerUrl){
    return this.http.get(this.blogApiUrl + '?blogger__link=' + bloggerUrl);
  }
  

}
