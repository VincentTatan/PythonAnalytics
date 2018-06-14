function setup(){
	noCanvas();
	frameRate(1)

	

	// const vtense = tf.variable(tense);
	// console.log(vtense);
	// tense.data().then(function(){
	// 	console.log(stuff);
	// });
	// console.log(tense.dataSync());
	// console.log(tense.get(0));

	// tense.set(0,10);

}

function draw(){
	const values = [];
		for (let i = 0;i<150000;i++){
			values[i]  = random(0,100);
		}

		const shape = [500,300];

		tf.tidy(=>{
			const a = tf.tensor2d(values,shape,'int32');
			const b = tf.tensor2d(values,shape,'int32');
			const b_t = b.transpose();

			const c = a.MatMul(b_t);
			console.log('hello');
		});

		//Do something meaningful.
		a.dispose();
		b.dispose();
		c.dispose();
		b_t.dispose();


		a.print();
		b.print();
		c.print();
	console.log
}