

const request = async (url, access_token) => {
    console.log(access_token);
    const response = await fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyIiwicm9sIjoidXNlciIsImVtYWlsIjoidXN1YXJpb0BleGFtcGxlLmNvbSIsImlkIjoxLCJwZXJtaXNzaW9ucyI6InBlcGl0byBjbGF2byB1biBjbGF2aXRvIiwiZXhwIjoxNzI4MTU5OTU3fQ.37nOhzXDMXAnCgvEubujvmSdw81oTHuRRRcYescrKu8",
            "token_type": "bearer"
        }),
    });
    const json = await response.json();
    return JSON.stringify(json);
}




fetch("https://ticketproject-dnku.onrender.com/auth/token", {
    method: "POST",
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        email: "usuario@example.com",
        password: "pass1234"
    }),
})
    .then((resp) => resp.json())
    .then(async (resp) => {
        localStorage.setItem("token", resp.access_token);
        let tree = await request('https://ticketproject-dnku.onrender.com/auth/login', resp.access_token);
        localStorage.setItem("user", tree)
        console.log(tree, 'este es data user');
    })
    .catch((e) => {
        console.warn("Error", e);
    })