import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AppoinmentList } from './appoinment-list';

describe('AppoinmentList', () => {
  let component: AppoinmentList;
  let fixture: ComponentFixture<AppoinmentList>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AppoinmentList]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AppoinmentList);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
