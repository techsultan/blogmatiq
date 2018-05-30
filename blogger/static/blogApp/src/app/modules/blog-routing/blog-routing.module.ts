import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';

//Import all components of blogApp 
import { HomeComponent } from '../../components/home/home.component';



const routes: Routes = [
 {
  path: '',
  component: HomeComponent
 }
]

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule],
  declarations: []
})
export class BlogRoutingModule { }
