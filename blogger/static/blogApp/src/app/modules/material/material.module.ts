import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {MatButtonModule, MatCardModule, MatToolbarModule, MatIconModule, 
    MatGridListModule, MatListModule} from '@angular/material';

@NgModule({
    imports: [MatButtonModule, MatCardModule, MatToolbarModule, 
        MatIconModule, MatGridListModule, MatListModule],
        
    exports: [MatButtonModule, MatCardModule, MatToolbarModule,
        MatIconModule, MatGridListModule, MatListModule]
})

export class MaterialModule { }