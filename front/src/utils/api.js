export const root = process.env.NODE_ENV === 'production' ? '/' : 'http://127.0.0.1:8000/'

export function api (url, opts = {}) {
  return (new Promise(async (resolve, reject) => {
    opts.credentials = opts.credentials || 'include'
    opts.headers = opts.headers || {}
    const resp = await fetch(root + url, opts)
    try {
      const dat = await resp.json()
      if (resp.status === 200) {
        return resolve(dat.data)
      } else {
        return reject(new Error(dat.msg))
      }
    } catch (e) {
      return reject(e)
    }
  })).catch(e => {
    throw e
  })
}
