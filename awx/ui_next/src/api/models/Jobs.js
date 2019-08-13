import Base from '../Base';

const BASE_URLS = {
  playbook: '/jobs/',
  project: '/project_updates/',
  system: '/system_jobs/',
  inventory: '/inventory_updates/',
  command: '/ad_hoc_commands/',
  workflow: '/workflow_jobs/',
};

class Jobs extends Base {
  constructor(http) {
    super(http);
    this.baseUrl = '/api/v2/jobs/';
  }

  readDetail(id, type) {
    return this.http.get(`/api/v2${BASE_URLS[type]}${id}/`);
  }

  readEvents(id, jobType = 'job', params = {}) {
    let endpoint;
    if (jobType === 'job') {
      endpoint = `${this.baseUrl}${id}/job_events/`;
    } else {
      endpoint = `${this.baseUrl}${id}/events/`;
    }
    return this.http.get(endpoint, { params });
  }
}

export default Jobs;
