function showform(event,formName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(formName).style.display = "block";
    event.currentTarget.className += " active";
}

function add_medical_history() {
	var form_idx = $('#id_form-TOTAL_FORMS').val();
	$('#first_medical_history_form').append($('#empty_medical_form').html().replace(/__prefix__/g, form_idx));
	$('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
}

function calculate_bmi() {
  var h = Number(document.getElementsByName('height')[0].value)/100;
  var w = Number(document.getElementsByName("weight")[0].value);
  var bmi;
  if ( h && w) {
      bmi = (w/(h*h)).toFixed(2);
  }
  document.getElementsByName("BMI")[0].value = bmi;
}

function enable_submit() {
  var x = document.getElementById('submit_button');
  x.disabled = false;
}

function calculate_EGDR() {
  var waist = Number(document.getElementsByName('waist')[0].value);
  var hip = Number(document.getElementsByName('hip')[0].value);
  var whr = (waist/hip);
  var htn;
  var SBP = Number(document.getElementsByName('systolic_BP')[0].value);
  var DBP = Number(document.getElementsByName('diastolic_BP')[0].value);
  var AHT_drug = document.getElementsByName('AntiHyperTensiveDrug')[0].value;
  var HbA1c = Number(document.getElementsByName('HbA1c')[0].value);
  console.log(whr);
  console.log(SBP);
  console.log(DBP);
  if ((SBP > 140) || (DBP > 90) || AHT_drug) {
    htn = 1;
  }
  else {
    htn = 0;
  }
  console.log(htn);
  console.log(AHT_drug);
  console.log(HbA1c);
  if ( whr && ((htn == 1) || (htn == 0)) && HbA1c) {
    var EGDR = 24.31 - (12.22*whr) - (3.29 * htn) - (0.57 * HbA1c);
    document.getElementsByName('EGDR')[0].value = EGDR.toFixed(2);
  }
  else {
    document.getElementsByName('EGDR')[0].value = "";
  }
}

function calculate_EGFR() {
  var age = Number(document.getElementsByName('age')[0].innerHTML);
  var cr = Number(document.getElementsByName('creatinine')[0].value);
  var sex = document.getElementsByName('sex')[0].innerHTML;
  var race = document.getElementsByName('race')[0].value;
  var alpha;
  var kappa;
  var EGFR;
  var sexFactor;
  var raceFactor;
  var ckd;
  if (sex == "M") {
    alpha = -0.411;
    kappa = 0.9;
    sexFactor = 1;
  }
  else if (sex == "F") {
    alpha = -0.329;
    kappa = 0.7;
    sexFactor = 1.018;
  }

  if (race == "black") {
    raceFactor = 1.159;
  }
  else {
    raceFactor = 1;
  }

  if (age && cr && sex && race && alpha && kappa && sexFactor && raceFactor) {
    EGFR = 141 * Math.pow(Math.min(cr/kappa,1.0),alpha) * Math.pow(Math.max(cr/kappa,1.0),-1.209) * Math.pow(0.993,age) * sexFactor * raceFactor;
    EGFR = Math.round(EGFR);
    if (EGFR > 90) {
      ckd = "1";
    }
    else if ((EGFR < 90) && (EGFR > 59)) {
      ckd = "2";
    }
    else if ((EGFR < 60) && (EGFR > 44)) {
      ckd = "3A";
    }
    else if ((EGFR < 45) && (EGFR > 29)) {
      ckd = "3B";
    }
    else if ((EGFR < 30) && (EGFR > 14)) {
      ckd = "4";
    }
    else {
      ckd = "5";
    }
  }
  else {
    EGFR = "";
    ckd = "";
  }
  document.getElementsByName('EGFR')[0].value = EGFR;
  document.getElementsByName('CKD_stage')[0].value = ckd;
}

function calculate_ascvd() {
  var age = Number(document.getElementsByName('age')[0].innerHTML);
  var sex = document.getElementsByName('sex')[0].innerHTML;
  var hdl = Number(document.getElementsByName('HDL')[0].value);
  var cholestrol = Number(document.getElementsByName('total_cholestrol')[0].value);
  var sbp = Number(document.getElementsByName('systolic_BP')[0].value);
  var antiHPDrug = document.getElementsByName('AntiHyperTensiveDrug')[0].value;
  var smoking;
  var score=0;
  var ascvd =0;
  console.log("AntiHPDrug = " + antiHPDrug)
  smoking_array = document.getElementsByName('smoking')
  if ((smoking_array[0].value == "1") && (smoking_array[0].checked == true)) {
    smoking = true;
    console.log("Smoking = True");
  }
  if ((smoking_array[0].value == "0") && (smoking_array[0].checked == true)) {
    smoking = false;
    console.log("Smoking = False");
  }
  if (sex == "M") {
    console.log("Sex = Male")
    if ((age >= 20) && (age <= 34)) {
      score = score -9;
      console.log("age group = 20-34");
      // Smoking Score
      if (smoking) {
        console.log("Smokes");
        score = score + 8;
      }
      // Cholestrol Score
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 4;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 7;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 9;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 11;
      }
      else {
        return;
      }
    }
    else if ((age >= 35) && (age <= 39)) {
      score = score -4;
      console.log("age group = 35-39");
      if (smoking) {
        console.log("Smokes");
        score = score + 8;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 4;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 7;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 9;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 11;
      }
      else {
        return;
      }
    }
    else if ((age >= 40) && (age <= 44)) {
      score = score + 0;
      console.log("age group = 40-44");
      if (smoking) {
        console.log("Smokes");
        score = score + 5;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 3;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 5;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 6;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 8;
      }
      else {
        return;
      }
    }
    else if ((age >= 45) && (age <= 49)) {
      score = score + 3;
      console.log("age group = 45-49");
      if (smoking) {
        console.log("Smokes");
        score = score + 5;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 3;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 5;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 6;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 8;
      }
      else {
        return;
      }
    }
    else if ((age >= 50) && (age <= 54)) {
      score = score + 6;
      console.log("age group = 50-54");
      if (smoking) {
        console.log("Smokes");
        score = score + 3;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 2;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 3;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 4;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 5;
      }
      else {
        return;
      }
    }
    else if ((age >= 55) && (age <= 59)) {
      score = score + 8;
      console.log("age group = 55-59");
      if (smoking) {
        console.log("Smokes");
        score = score + 3;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 2;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 3;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 4;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 5;
      }
      else {
        return;
      }
    }
    else if ((age >= 60) && (age <= 64)) {
      score = score + 10;
      console.log("age group = 60-64");
      if (smoking) {
        console.log("Smokes");
        score = score + 1;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 1;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 1;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 2;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 3;
      }
      else {
        return;
      }
    }
    else if ((age >= 65) && (age <= 69)) {
      score = score + 11;
      console.log("age group = 65-69");
      if (smoking) {
        console.log("Smokes");
        score = score + 1;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 1;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 1;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 2;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 3;
      }
      else {
        return;
      }
    }
    else if ((age >= 70) && (age <= 74)) {
      score = score + 12;
      console.log("age group = 70-74");
      if (smoking) {
        console.log("Smokes");
        score = score + 1;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 0;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 0;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 1;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 1;
      }
      else {
        return;
      }
    }
    else if ((age >= 75) && (age <= 79)) {
      score = score + 13;
      console.log("age group = 75-79");
      if (smoking) {
        console.log("Smokes");
        score = score + 1;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 0;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 0;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 1;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 1;
      }
      else {
        return;
      }
    }
    else {
      return;
    }
    // HDL Score
    if (hdl >= 60) {
      score = score -1;
    }
    else if ((hdl >= 50) && (hdl <= 59)) {
      score = score + 0;
    }
    else if ((hdl >= 40) && (hdl <= 49)) {
      score = score + 1;
    }
    else if (hdl < 40) {
      score = score + 2;
    }
    else {
      return;
    }
    if ((sbp >= 120) && (sbp <= 129)) {
      if (antiHPDrug == "1") {
        score =score + 1;
      }
      else {
        score = score + 0;
      }
    }
    else if ((sbp >= 130) && (sbp <= 139)) {
      if (antiHPDrug == "1") {
        score =score + 2;
      }
      else {
        score = score + 1;
      }
    }
    else if ((sbp >= 140) && (sbp <= 159)) {
      if (antiHPDrug == "1") {
        score =score + 2;
      }
      else {
        score = score + 1;
      }
    }
    else if (sbp > 160) {
      if (antiHPDrug == "1") {
        score =score + 3;
      }
      else {
        score = score + 2;
      }
    }
    else {
      return;
    }
    if (score == 0) {
      ascvd = 0;
    }
    else if ((score >=1) && (score <= 4)) {
      ascvd = 1;
    }
    else if ((score >=5) && (score <= 6)) {
      ascvd = 2;
    }
    else if ((score == 7)) {
      ascvd = 3;
    }
    else if ((score == 8)) {
      ascvd = 4;
    }
    else if ((score == 9)) {
      ascvd = 5;
    }
    else if ((score == 10)) {
      ascvd = 6;
    }
    else if ((score == 11)) {
      ascvd = 8;
    }
    else if ((score == 12)) {
      ascvd = 10;
    }
    else if ((score == 13)) {
      ascvd = 12;
    }
    else if ((score == 14)) {
      ascvd = 16;
    }
    else if ((score == 15)) {
      ascvd = 20;
    }
    else if ((score == 16)) {
      ascvd = 25;
    }
    else if ((score >= 17)) {
      ascvd = 30;
    }
    else {
      return;
    }
    document.getElementsByName("ASCVD_Score")[0].value = ascvd;
  }
  if (sex == "F") {
    console.log("Sex = Female")
    if ((age >= 20) && (age <= 34)) {
      score = score -7;
      console.log("age group = 20-34");
      // Smoking Score
      if (smoking) {
        console.log("Smokes");
        score = score + 9;
      }
      // Cholestrol Score
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 4;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 8;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 11;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 13;
      }
      else {
        return;
      }
    }
    else if ((age >= 35) && (age <= 39)) {
      score = score -3;
      console.log("age group = 35-39");
      if (smoking) {
        console.log("Smokes");
        score = score + 9;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 4;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 8;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 11;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 13;
      }
      else {
        return;
      }
    }
    else if ((age >= 40) && (age <= 44)) {
      score = score + 0;
      console.log("age group = 40-44");
      if (smoking) {
        console.log("Smokes");
        score = score + 7;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 3;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 6;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 8;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 10;
      }
      else {
        return;
      }
    }
    else if ((age >= 45) && (age <= 49)) {
      score = score + 3;
      console.log("age group = 45-49");
      if (smoking) {
        console.log("Smokes");
        score = score + 7;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 3;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 6;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 8;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 10;
      }
      else {
        return;
      }
    }
    else if ((age >= 50) && (age <= 54)) {
      score = score + 6;
      console.log("age group = 50-54");
      if (smoking) {
        console.log("Smokes");
        score = score + 4;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 2;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 4;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 5;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 7;
      }
      else {
        return;
      }
    }
    else if ((age >= 55) && (age <= 59)) {
      score = score + 8;
      console.log("age group = 55-59");
      if (smoking) {
        console.log("Smokes");
        score = score + 4;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 2;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 4;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 5;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 7;
      }
      else {
        return;
      }
    }
    else if ((age >= 60) && (age <= 64)) {
      score = score + 10;
      console.log("age group = 60-64");
      if (smoking) {
        console.log("Smokes");
        score = score + 2;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 1;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 2;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 3;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 4;
      }
      else {
        return;
      }
    }
    else if ((age >= 65) && (age <= 69)) {
      score = score + 12;
      console.log("age group = 65-69");
      if (smoking) {
        console.log("Smokes");
        score = score + 2;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 1;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 2;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 3;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 4;
      }
      else {
        return;
      }
    }
    else if ((age >= 70) && (age <= 74)) {
      score = score + 14;
      console.log("age group = 70-74");
      if (smoking) {
        console.log("Smokes");
        score = score + 1;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 1;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 1;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 2;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 2;
      }
      else {
        return;
      }
    }
    else if ((age >= 75) && (age <= 79)) {
      score = score + 16;
      console.log("age group = 75-79");
      if (smoking) {
        console.log("Smokes");
        score = score + 1;
      }
      if ((cholestrol >= 160) && (cholestrol <= 199)) {
        console.log("Cholestrol 1");
        score = score + 1;
      }
      else if ((cholestrol >= 200) && (cholestrol <= 239)) {
        console.log("Cholestrol 2");
        score = score + 1;
      }
      else if ((cholestrol >= 240) && (cholestrol <= 279)) {
        console.log("Cholestrol 3");
        score = score + 2;
      }
      else if (cholestrol >= 280) {
        console.log("Cholestrol 4");
        score = score + 2;
      }
      else {
        return;
      }
    }
    else {
      return;
    }
    // HDL Score
    if (hdl >= 60) {
      score = score -1;
    }
    else if ((hdl >= 50) && (hdl <= 59)) {
      score = score + 0;
    }
    else if ((hdl >= 40) && (hdl <= 49)) {
      score = score + 1;
    }
    else if (hdl < 40) {
      score = score + 2;
    }
    else {
      return;
    }
    // Systolic BP Score
    if ((sbp >= 120) && (sbp <= 129)) {
      if (antiHPDrug == "1") {
        score =score + 3;
      }
      else {
        score = score + 1;
      }
    }
    else if ((sbp >= 130) && (sbp <= 139)) {
      if (antiHPDrug == "1") {
        score =score + 4;
      }
      else {
        score = score + 2;
      }
    }
    else if ((sbp >= 140) && (sbp <= 159)) {
      if (antiHPDrug == "1") {
        score =score + 5;
      }
      else {
        score = score + 3;
      }
    }
    else if (sbp > 160) {
      if (antiHPDrug == "1") {
        score =score + 6;
      }
      else {
        score = score + 4;
      }
    }
    else {
      return;
    }
    if (score < 9) {
      ascvd = 0;
    }
    else if ((score >=9) && (score <= 12)) {
      ascvd = 1;
    }
    else if ((score >=13) && (score <= 14)) {
      ascvd = 2;
    }
    else if ((score == 15)) {
      ascvd = 3;
    }
    else if ((score == 16)) {
      ascvd = 4;
    }
    else if ((score == 17)) {
      ascvd = 5;
    }
    else if ((score == 18)) {
      ascvd = 6;
    }
    else if ((score == 19)) {
      ascvd = 8;
    }
    else if ((score == 20)) {
      ascvd = 11;
    }
    else if ((score == 21)) {
      ascvd = 14;
    }
    else if ((score == 22)) {
      ascvd = 17;
    }
    else if ((score == 23)) {
      ascvd = 22;
    }
    else if ((score == 24)) {
      ascvd = 27;
    }
    else if ((score >= 25)) {
      ascvd = 30;
    }
    else {
      return;
    }
    document.getElementsByName("ASCVD_Score")[0].value = ascvd;
  }
}

function ad_search_val(event) {
  var el= document.getElementById('id_search').value;
  var val1 = document.getElementById('value1');
  var val2 = document.getElementById('value2');
  if(el == "ckd_stage") {
    val1.style.display = "block";
    val2.style.display = "none";
  }
  else {
    if(el == ""){
      val1.style.display = "none";
      val2.style.display = "none";
    }
    else {
      val1.style.display = "block";
      val2.style.display = "block";
    }
  }
  
}