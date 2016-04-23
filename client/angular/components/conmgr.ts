import {Component, OnInit} from 'angular2/core';
import {NgClass, CORE_DIRECTIVES} from 'angular2/common';
import {Alert} from 'ng2-bootstrap/ng2-bootstrap';

import {Container} from '../shared/container';

import {ContainerService} from '../services/containerService';

@Component({
    selector: 'conmgr',
    directives: [Alert, NgClass, CORE_DIRECTIVES],
    templateUrl: 'angular/templates/conmgr.html',
    providers: [ContainerService]
})
export class ConmgrComponent implements OnInit {
  containers: Container[] = [];
  pending: boolean = false;
  alerts: Object[] = [];

  constructor(private _containerService: ContainerService) {}

  ngOnInit() {
    this.refresh();
  }

  startStop(container) {
    this.pending = true;
    if (container.running) {
      this._containerService.stopContainer(container.id).subscribe(
        res => container.running = false,
        err => this.addAlert('Stop failed!'),
        () => this.pending = false
      );
    } else {
      this._containerService.startContainer(container.id).subscribe(
        res => container.running = true,
        err => this.addAlert('Start failed!'),
        () =>  this.pending = false
      );
    }
  }

  refresh() {
    this.pending = true;
    this._containerService.getContainers().subscribe(
      containers => this.containers = containers,
      err => this.addAlert('Refresh failed!'),
      () => this.pending = false
    );
  }

  addAlert(msg: string) {
    this.alerts.push({msg: msg, type: 'danger', closable: true})
  }

  closeAlert(alertIndex) {
    this.alerts.splice(alertIndex, 1);
  }
}
