const express = require('express');
const app = express();
app.use(express.json());
app.post('/api/v1/payment/create', (req,res)=>res.json({status:'success',data:req.body}));
app.listen(3000, ()=>console.log('API Gateway running'));