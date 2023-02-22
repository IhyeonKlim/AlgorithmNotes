/* 
    which accepts two arrays.
    the function should return true 
    if every value in the array has it's corresponding value
    squared in the socond array.
    
*/

same([1,2,3], [4,1,9]) //true
same([1,2,3], [1,9])   //false
same([1,2,1], [4,4,1]) //false(must be same frequency)



function same(array1, array2){
    var flag = false;
    if (array1.legnth !== array2.length){
        return false;
    }
    for (var i = 0; i < array1.length; i ++){
        let correctIndex = array2.indexOf(array1[i]**2)
        //cf. array.indexOf(); -> find index of value.  
        if(correctIndex === -1){
            return false;
        }
        //array.indexOf() if there is none. return -1.
        //console.log(array2) -> 줄어드는 배열의 길이를 볼 수 있다.
        array2.splice(correctIndex,1)
        //cf. function splice(indexNo, deleteElementCount, addValue);
        //ex, array.splice(0,0,'sample')-> 0번 인덱스에 sample 추가
        //ex, array.splice(3,1) -> 3번 인덱스에 1개 요소 제거
        //ex, array.splice(2,1,'smaple') 2번인덱스에서 하나 제거 후 거기다 sample 추가 
        //ex, array.splice(0,2,'t1','t2,'t3) 0번 인덱스의 2개 제거 후 t1~t3 추가
        //ex, array.splice(-2,1) -2번 인덱스 = array.length -2 의 인덱스. 즉, 오른쪽에서 2번째. 인덱스 1개 제거
        //ex, array.splice(-1,3) 가장 오른쪽 인덱스로부터 3개. -> 모순. 따라서 제일 끝 인자 1개만 제거된다..
        //return -> 자른 녀석을 반환, 단, 자른녀석이 없다면 빈 배열을 반환한다.
    }
    return flag;
}

//refactored.

function r_same(arr1, arr2){
    if(arr1.length !== arr2.length){
        return false;
    }
    let frequencyCounter1 = {}
    let frequencyCounter2 = {}
    
    //각각의 루프는 같은 내용의 val을 키형태로 집어넣어서 몇개나 되는지 빈도를 체크한다.
    for(let val of arr1){
        frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1
    }
    
    for(let val of arr2){
        frequencyCounter2[val] = (frequencyCounter2[val] || 0) + 1
    }
    //중첩된 개별 루프보다 각각의 두개의 루프가 훨씬 낫다.
    //시간복잡도 -> O(2N)이다.
    //중첩된 루프는 -> O(N^)이다.
    consoel.log(frequencyCounter1);
        consoel.log(frequencyCounter2);
    for(let key in frequencyCounter1){
        //일단 제곱한 녀석이 있는지 확인.
        if(!(key ** 2 in frequencyCounter2)){
            return false
        }
        //있다면 몇개 있는지를 확인.
        if(frequencyCounter2[key**2] !== frequencyCounter1[key]){
            return false
        }
    }
    return true
}
/*해당방법은 시간복잡도 면에서 월등하다.
빈도 카운터의 개념은 보통 객체를 사용한다는 것이다.
객체를 사용하여 프로파일을 구성하는 것은 
배열이나 문자열의 내용을 분석하는 방법으로 
보통 배열이나 문자열과 같은 선형구조로 만드는 것이다.
그러면 해당 분석을 다른객체와 신속하게 비교할 수있다.
*/
