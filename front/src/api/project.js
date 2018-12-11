import requests from '@/utils/requests'

export function fetchList () {
  return requests({
    url: '/project',
    method: 'get'
  })
}
