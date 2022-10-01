API_PATH = '/api/user'

export const getUser = async () => {
    return { 'id': 1, 'username': 'ndifreke@gmail.com', 'first_name': 'ndifreke' }
    // const resp = await fetch(API_PATH)
    // return resp.json()
}