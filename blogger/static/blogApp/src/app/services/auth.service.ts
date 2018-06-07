import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  authUrl:string;

  constructor(private Http: HttpClient) { 

  }

  login(){
    //Fully implement this using HttpInterceptors
    return "Logged in!";
  }
}
