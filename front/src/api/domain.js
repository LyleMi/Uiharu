import requests from '@/utils/requests'

export function getDomains () {
  return requests({
    url: '/domain',
    method: 'get'
  })
}

export function createDomain (data) {
  return requests({
    url: '/domain',
    method: 'post',
    data
  })
}

export function deleteDomain (query) {
  return requests({
    url: '/domain',
    method: 'delete',
    params: query
  })
}
