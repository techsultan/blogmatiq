import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class BlogService {

  bloApiUrl:string = "/api/blogs/";

  constructor(private Http: HttpClient) { }


}
