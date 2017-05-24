import { fetchData, setParams } from './api/actions';
import store from './store';
import { events } from './events';

export default function(){
  store.dispatch(setParams('programData', { endpoint: 'program' } ));
  store.dispatch(fetchData('programData'));

  store.dispatch(setParams('contentTypes', { endpoint: 'content-types' }));
  store.dispatch(fetchData('contentTypes'));

  events.scrollPosition();
}
