import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddNewListFormComponent } from './add-new-list-form.component';

describe('AddNewListFormComponent', () => {
  let component: AddNewListFormComponent;
  let fixture: ComponentFixture<AddNewListFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddNewListFormComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddNewListFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
