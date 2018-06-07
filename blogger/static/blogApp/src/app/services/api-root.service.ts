import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiRootService {

  DEV_API_ROOT = "http://localhost:8000";
  constructor() { }

  getRoot(){
  if (environment.production){
    return "";
  }
  else{
    return this.DEV_API_ROOT;
  }
}



}
