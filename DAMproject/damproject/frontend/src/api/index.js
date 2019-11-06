import axios from 'axios'
import qs from 'qs'

class Base {
  constructor () {
    this.$http = axios.create({
      withCredentials: true
    })

    this.dataMethodDefaults = {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest'
      },
      transformRequest: [function (data) {
        return qs.stringify(data, {indices: false})
      }]
    }
  }

  get (url, config = {}) {
    return this.$http.get(url, config)
  }

  post (url, data = undefined, config = {}) {
    if (process.env.NODE_ENV === 'development') {
      url = '/api/' + url
    }
    return this.$http.post(url, data, { ...this.dataMethodDefaults, ...config })
  }

  put (url, data = undefined, config = {}) {
    return this.$http.put(url, data, { ...this.dataMethodDefaults, ...config })
  }

  delete (url, config = {}) {
    return this.$http.delete(url, config)
  }
}

export default new Base()
