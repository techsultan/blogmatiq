import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ApiRootService } from './api-root.service';

@Injectable({
  providedIn: 'root'
})
export class BlogCategoryService {
  categoryApiUrl: string;
  blog_category_api:string = "/api/blogger/blogcategories/";

  constructor(private http:HttpClient, private ApiRoot: ApiRootService) {
    this.categoryApiUrl = this.ApiRoot.getRoot() + this.blog_category_api;
   }

  getCategoriesByBlog(blogUrl){
    return this.http.get(this.categoryApiUrl+ '?blog__link='+blogUrl);
  }

  getCategoryByUrl(categoryUrl){
    return this.http.get(this.categoryApiUrl+categoryUrl);
  }

  createCategory(new_category_data){
    return this.http.post(this.categoryApiUrl, new_category_data);
  }

  updateCategory(categoryUrl, updated_category_data){
    return this.http.put(this.categoryApiUrl+categoryUrl, updated_category_data);
  }

  deleteCategory(categoryUrl){
    return this.http.delete(this.categoryApiUrl+categoryUrl);
  }
}
