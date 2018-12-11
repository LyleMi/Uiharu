import requests from '@/utils/requests'

export function getProjects () {
  return requests({
    url: '/project',
    method: 'get'
  })
}

export function createProject (data) {
  return requests({
    url: '/project',
    method: 'post',
    data
  })
}

export function deleteProject (query) {
  return requests({
    url: '/project',
    method: 'delete',
    params: query
  })
}
