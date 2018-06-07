import { ApiRootService } from './api-root.service';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';



@Injectable({
  providedIn: 'root'
})
export class BlogPostService {

  blogPostApiUrl: string;
  blogpost_api:string = "/api/blog/blogposts/";

  constructor(private http:HttpClient, private ApiRoot: ApiRootService) {
    this.blogPostApiUrl = this.ApiRoot.getRoot() + this.blogpost_api;
   }

  getAllPosts(){
    return this.http.get(this.blogPostApiUrl);
  }

  getPostsinBlog(blogUrl){
    return this.http.get(this.blogPostApiUrl+'?category__blog__link='+blogUrl);
  }

  getPost(postUrl){
    return this.http.get(this.blogPostApiUrl+postUrl);
  }

  getPostsInCategory(categoryUrl){
    return this.http.get(this.blogPostApiUrl+'?category__link='+categoryUrl);
  }

  createPost(new_post_data){
    return this.http.post(this.blogPostApiUrl, new_post_data);
  }

  updatePost(postUrl, new_post_data){
    return this.http.put(this.blogPostApiUrl+postUrl, new_post_data);
  }

  deletePost(postUrl){
    return this.http.delete(this.blogPostApiUrl+postUrl);
  }


}
