import { ApiRootService } from './api-root.service';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})

export class BloggerService {
  bloggerApiUrl:string;
  blogger_api:string = "/api/blog/bloggers/";

  constructor(private http:HttpClient, private ApiRoot: ApiRootService) {
    this.bloggerApiUrl = this.ApiRoot.getRoot() + this.blogger_api;
   }

  getBlogger(bloggerUrl){
    return this.http.get(this.bloggerApiUrl+bloggerUrl);
  }

  getAllBloggers(){
    return this.http.get(this.bloggerApiUrl);
  }

  createBlogger(new_blogger_data){
    return this.http.post(this.bloggerApiUrl, new_blogger_data);
  }

  updateBlogger(bloggerUrl, updated_blogger_data){
    return this.http.put(this.bloggerApiUrl + bloggerUrl, updated_blogger_data);
  }

  deleteBlogger(bloggerUrl){
    return this.http.delete(this.bloggerApiUrl + bloggerUrl);
  }

  getPostsByBlogger(bloggerUrl){
    return this.http.get("/api/blog/blogposts?category__blog__blogger__link="+bloggerUrl);
  }


}
