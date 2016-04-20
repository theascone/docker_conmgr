import {bootstrap} from 'angular2/platform/browser';
import {HTTP_PROVIDERS} from 'angular2/http';

import {ConmgrComponent} from './components/conmgr';

bootstrap(ConmgrComponent, [ HTTP_PROVIDERS ]);
